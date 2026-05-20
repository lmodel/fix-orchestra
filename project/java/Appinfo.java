package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Usage specific annotation, optionally with link to an external reference or standard
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Appinfo  {

  private URI specUrl;
  private String value;
  private List<String> content;
  private List<String> extraAttributes;
  private String langId;
  private String purpose;
  private String added;
  private String addedEp;
  private String changeType;
  private String deprecatedEp;
  private String issue;
  private String lastModified;
  private String replaced;
  private String replacedEp;
  private String replacedByField;
  private String supported;
  private String updated;
  private String updatedEp;
  private String deprecated;


}