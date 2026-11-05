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
  An XML attribute from another namespace, kept as written.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraXmlAttribute  {

  private String xmlName;
  private String xmlValue;


}