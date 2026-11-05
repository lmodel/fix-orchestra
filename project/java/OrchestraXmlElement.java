package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An XML element in a place where the XSDs accept any content, kept as written so that the file converts back unchanged.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraXmlElement  {

  private String xmlName;
  private List<OrchestraXmlAttribute> xmlAttributes;
  private String xmlText;
  private List<OrchestraXmlElement> xmlChildren;
  private String xmlTail;


}