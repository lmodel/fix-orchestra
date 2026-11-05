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
  A hint for a particular tool or encoding, such as how FIXML renders an element, held as text and open XML.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraAppinfoV10  {

  private String fixrText;
  private List<OrchestraXmlElement> fixrAny;
  private URI fixrSpecUrl;
  private String fixrLangId;
  private String fixrPurpose;
  private List<OrchestraXmlAttribute> fixrOtherAttributes;
  private String fixrAdded;
  private Integer fixrAddedEp;
  private String fixrChangeType;
  private String fixrDeprecated;
  private Integer fixrDeprecatedEp;
  private String fixrIssue;
  private String fixrLastModified;
  private String fixrReplaced;
  private Integer fixrReplacedEp;
  private Integer fixrReplacedByField;
  private String fixrSupported;
  private String fixrUpdated;
  private Integer fixrUpdatedEp;


}